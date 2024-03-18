import logging
import requests


from QA_Model.QA_Model import answering_model
from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message
from keyboards.keyboards import filled_form_kb


logger = logging.getLogger(__name__)

router = Router()


class FSMFillQuestion(StatesGroup):
    fill_question = State()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет! Я твой бот, который поможет вам выбрать вопрос о нашей компании '
                         'и нейросеть попробует на него ответить!',
                         reply_markup=filled_form_kb())


@router.message()
async def fill_question(message: Message):
    question = str(message.text)
    await message.answer(answering_model(question)['answer'])

'''
Думаю функционал ниже сдесь не особо нужен
'''



@router.message(F.text == 'QA_BTN🤖')
async def vent_ai_btn(message: Message, state: FSMContext):
    await message.answer('Вы можете задать вопрос о нашей компании '
                         'и нейросеть попробует на него ответить!')
    await state.set_state(FSMFillQuestion.fill_question)


@router.message(F.text, StateFilter(FSMFillQuestion.fill_question))
async def fill_question(message: Message, state: FSMContext):
    question = str(message.text)
    await message.answer(answering_model(question)['answer'])
    await state.clear()


@router.message(StateFilter(FSMFillQuestion.fill_question))
async def fill_question_problem(message: Message):
    await message.answer('Пожалуйста, напишите вопрос который вас интересует,'
                         '(фото, видео, файлы, и др. не поддерживается)')
