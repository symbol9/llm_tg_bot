from transformers import pipeline


def answering_model(question):
    qa_model = pipeline(
        'question-answering',
        model='Den4ikAI/rubert_large_squad_2',
        tokenizer='Den4ikAI/rubert_large_squad_2')
    with open(r'C:\Users\nefio\PycharmProjects\llm_tg_bot\QA_Model\data_2.txt', 'r', encoding='utf-8') as data_file:
        context_1 = data_file.read()
    with open(r'C:\Users\nefio\PycharmProjects\llm_tg_bot\QA_Model\prompt.txt', 'r', encoding='utf-8') as prompt_file:
        prompt = prompt_file.read()
    res = qa_model({
        'context': prompt + context_1,
        'question': question
    })

    return res
