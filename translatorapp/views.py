from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
import openai

openai.api_key = "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"


def translate(request):



    if request.method == 'POST':
        source_text = request.POST.get('source_text')
        target_lang = request.POST.get('target_lang')

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="translate from {} to {}: {}".format('en', target_lang, source_text),
            temperature=0.5,
            max_tokens=4000
        )

        translation = response.choices[0].text
        print(translation)

        return render(request, 'translatorapp/translate.html', {'translation': translation})

    return render(request, 'translatorapp/translate.html')