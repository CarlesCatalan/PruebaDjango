import requests
from django.conf import settings
from django.shortcuts import render, redirect
import PruebaDjango.settings as settings


def _build_contents(chat_history, new_user_text):
    contents = []
    for item in chat_history[-10:]:
        role = item.get('role')
        text = item.get('text', '').strip()
        if role in ('user', 'model') and text:
            contents.append({'role': role, 'parts': [{'text': text}]})

    contents.append({'role': 'user', 'parts': [{'text': new_user_text}]})
    return contents


def _extract_reply(response_json):
    candidates = response_json.get('candidates', [])
    if not candidates:
        return ''

    content = candidates[0].get('content', {})
    parts = content.get('parts', [])
    if not parts:
        return ''

    return (parts[0].get('text') or '').strip()


def ia_chat(request):
    chat_history = request.session.get('ia_chat_history', [])
    error = ''

    if request.method == 'POST':
        if 'clear_chat' in request.POST:
            request.session['ia_chat_history'] = []
            return redirect('ia_chat')

        user_message = request.POST.get('mensaje', '').strip()

        if not user_message:
            error = 'Escribe un mensaje antes de enviar.'
        elif not settings.GOOGLE_AI_API_KEY:
            error = 'Falta GOOGLE_AI_API_KEY en tu .env.'
        else:
            # elige aquí el modelo correcto (ver pasos siguientes)
            # <- sustituye por el valor de models.list
            model_name = "models/gemini-2.5-flash"
            endpoint = f"https://generativelanguage.googleapis.com/v1beta/{model_name}:generateContent"

            system_prompt = request.POST.get('system_prompt', '').strip()
            if system_prompt:
                request.session['ia_chat_system_prompt'] = system_prompt
            system_prompt = request.session.get('ia_chat_system_prompt', '')

            # Hardcodea aquí cómo debe comportarse el asistente

            payload = {'contents': _build_contents(chat_history, user_message)}
            payload['systemInstruction'] = {
                'parts': [{'text': settings.SYSTEM_PROMPT}]}
            payload['generationConfig'] = {
                'maxOutputTokens': 512, 'temperature': 0.6}

            headers = {
                'x-goog-api-key': settings.GOOGLE_AI_API_KEY,
                'Content-Type': 'application/json',
            }

            try:
                response = requests.post(
                    endpoint, headers=headers, json=payload, timeout=30)
                response.raise_for_status()
                model_text = _extract_reply(response.json())

                if model_text:
                    chat_history.append({'role': 'user', 'text': user_message})
                    chat_history.append({'role': 'model', 'text': model_text})
                    request.session['ia_chat_history'] = chat_history[-20:]
                    return redirect('ia_chat')

                error = 'La IA no devolvió texto en la respuesta.'
            except requests.RequestException as exc:
                error = f'Error llamando a Google AI Studio: {exc}'

    return render(
        request,
        'ia_chat/chat.html',
        {
            'chat_history': chat_history,
            'error': error,
        },
    )
