from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from habits.models import Habit
from habits.paginations import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer



class HabitsCreateAPIView(generics.CreateAPIView):
    """ Создание привычки
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """ Добавляем текущего пользователя
        в качест ве владельца привычки"""
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitsListAPIView(generics.ListAPIView):
    """ Отображение привычек пользователя
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = HabitPaginator

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр выбранной привычки
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class HabitsUpdateAPIView(generics.UpdateAPIView):
    """ Обновление выбранной привычки
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)

    def perform_update(self, serializer):
        habit = serializer.save()
        habit.save()


class HabitsDestroyAPIView(generics.DestroyAPIView):
    """ Удаление выбранной привычки
     """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)



class PublicHabitListAPIView(generics.ListAPIView):
    """ Список публичных привычек
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    pagination_class = HabitPaginator
    permission_classes = (AllowAny,)
