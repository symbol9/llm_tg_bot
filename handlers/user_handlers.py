import logging
import QA_Model

from aiogram.types import Message
from aiogram.dispatcher.filters.state import State, StateFilter
from aiogram.dispatcher.filters import Filters as F
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.filters import CommandStart


logger = logging.getLogger(__name__)

router = Router()


class FSMFillQuestion(StatesGroup):
    fill_question = State()


@router.message(CommandStart)
async def start(message: Message):
    await message.answer('Привет! Я твой бот, который поможет вам выбрать вопрос о нашей компании '
                         'и нейросеть попробует на него ответить!',
                         reply_markup=QA_Model.get_keyboard())


@router.message(F.text == 'QA_BTN🤖')
async def vent_ai_btn(message: Message):
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
