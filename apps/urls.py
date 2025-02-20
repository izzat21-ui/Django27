from django.urls import path

from apps.views import FilmView, TodoFormView, DelTodoView, TodoCreateView, CarsView, RegisterFormView, \
    HomePageView, IncomeFormView, LoginFormView, HomeFormView

# from apps.views import home_view, film_view, todo_del_view, del_todo_view



urlpatterns = [
    # path("", HomeListView.as_view()),
    path('film', FilmView.as_view(), name='film-home'),
    path('cars', CarsView.as_view(), name='cars-home'),
    path('todo/create', TodoCreateView.as_view(), name='todo-create'),
    path('todo/list', TodoFormView.as_view(), name='todo_list'),
    path('tododel', DelTodoView.as_view(), name='todo_del'),
    path("register", RegisterFormView.as_view(), name='register'),
    path("home", HomePageView.as_view(), name='home'),
    path('income', IncomeFormView.as_view(), name='income'),
    # path('logout', LogoutFormView.as_view(), name='logout'),
    path("", LoginFormView.as_view(), name='login-html'),
    path("Home/list", HomeFormView.as_view(), name='user'),
    # path("sahifa/list", SahifaFormView.as_view(), name='bosh_sahifa'),
    # path('logout', logout_view, name='logout'),

]
