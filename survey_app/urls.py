from django.urls import path

from . import apiviews


app_name = 'survey_app'
urlpatterns = [
    path('login/', apiviews.login, name='login'),
    # Опросы (surveys)
    path('survey_app/create/', apiviews.survey_create, name='survey_create'),
    path('survey_app/update/<int:survey_id>/', apiviews.survey_update, name='survey_update'),
    path('survey_app/view/', apiviews.survey_view, name='survey_view'),
    path('survey_app/view/active/', apiviews.active_survey_view, name='active_survey_view'),
    # Вопрос (question)
    path('question/create/', apiviews.question_create, name='question_create'),
    path('question/update/<int:question_id>/', apiviews.question_update, name='question_update'),
    # Выбор (choice)
    path('choice/create/', apiviews.choice_create, name='choice_create'),
    path('choice/update/<int:choice_id>/', apiviews.choice_update, name='choice_update'),
    # Ответ (answer)
    path('answer/create/', apiviews.answer_create, name='answer_create'),
    path('answer/view/<int:user_id>/', apiviews.answer_view, name='answer_view'),
    path('answer/update/<int:answer_id>/', apiviews.answer_update, name='answer_update')

]

