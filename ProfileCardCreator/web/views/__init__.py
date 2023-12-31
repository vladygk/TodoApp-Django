from .auth_views import RegisterView, LoginView, LogoutView, IndexView
from .task import TasksListView, CreateTaskView, TaskDeleteView, TaskMarkAsDoneView, TodoTaskUpdateView
from .category import CategoryListView, CategoryCreateView, CategoryDeleteView
from .fields_of_work import FieldOfWorkListView, FieldOfWorkCreateView, FieldOfWorkDeleteView
from .subtask import SubtaskCreateView, SubtaskListView, SubtaskDeleteView
from .item import ItemCreateView, ItemDetailView, ItemListView, ItemDeleteView
from .error import Custom403View, Custom404View
from .authorization import AddUserToGroupView, RemoveUserToGroupView

