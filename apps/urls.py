from django.urls import path

from apps.views import FilmView, TodoFormView, DelTodoView, TodoCreateView, CarsView, RegisterFormView, \
    HomePageView, IncomeFormView, LoginFormView, HomeFormView

# from apps.views import home_view, film_view, todo_del_view, del_todo_view



urlpatterns = [
    # path("", HomeListView.as_view()),
    path("register", RegisterFormView.as_view(), name='register'),
    path("home", HomePageView.as_view(), name='home'),
    path('income', IncomeFormView.as_view(), name='income'),
    path("", LoginFormView.as_view(), name='login-html'),
    path("Home/list", HomeFormView.as_view(), name='user'),
    

]
