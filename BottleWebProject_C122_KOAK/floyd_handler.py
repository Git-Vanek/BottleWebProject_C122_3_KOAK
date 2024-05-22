from bottle import route, run, template, post, request
from datetime import datetime
import numpy as np
import createGraph
import save_history
import math

@post('/floyd_result', method='POST')
def getResult():
    """
    Обрабатывает данные из формы, вычисляет кратчайшие расстояния по алгоритму Флойда-Уоршелла, 
    создает визуализацию графа и возвращает результат на шаблон.
    """
     # Получает размер матрицы из формы
    size = int(request.forms.get('matrix_size'))
    # Создает матрицу нулей размерности size x size
    matrix = np.zeros((size, size))
    # Заполняет матрицу значениями из формы 
    for i in range(size):
        for j in range(size):
            if request.forms.get('matrix[%i][%i]'%(i, j)) == "":    
            # Если не была введено значение между вершинами - присваиваем бесконечность
                if(i != j):
                    matrix[i, j] = math.inf
                # Иначе - 0
                else:
                    matrix[i, j] = 0
            else:
                # Получение данных
                if ( int(request.forms.get('matrix[%i][%i]'%(i, j))) == 0 and i != j):
                    matrix[i, j] = math.inf
                else:
                    matrix[i, j] = int(request.forms.get('matrix[%i][%i]'%(i, j)))
    
    # Создаёт массив из начальной и итоговой матрицы для сохранения в историю
    savedata = [matrix.tolist(), floydmethod(matrix).tolist()]
    # Вычисляет кратчайшие расстояния между всеми парами вершин
    matrix = floydmethod(matrix)
    # Сохраняет данные в json-файле
    save_history.createhistory("Floyda", savedata)
    # Создает визуализацию графа
    createGraph.createGraph(matrix, [])
    # Возвращает результат на шаблон "result.tpl"
    return template('result.tpl',title='Floyd method result',
        message='Ниже представлен ваш граф, вычисленный по методу Флойда.',
        year=datetime.now().year, data=matrix)

def floydmethod(V):
    """
    Реализует алгоритм Флойда-Уоршелла для вычисления кратчайших расстояний между всеми парами вершин в графе.
    """
    # Получает размер матрицы смежности
    N = len(V)
    # количество элементов в строке 
    amountofelements = len(V[0])
    # если количество вершин не равно количество элементов в строке, то вызывать исключение ValueError
    if(N != amountofelements):
        raise ValueError("Введена не квадратная матрица!")
    # если размерность матрицы меньше 3 или больше 10, то вызывать исключение ValueError
    if(N < 3 or N > 10):
        raise ValueError("Размерность матрицы должна быть в пределе от 3 до 10!")
    # Алгоритм Флойда-Уоршелла:
    for k in range(N): # Цикл по всем вершинам k (промежуточные вершины)
        for i in range(N): # Цикл по всем вершинам i (начальные вершины)
            for j in range(N): # Цикл по всем вершинам j (конечные вершины)
                # Вычисляет кратчайшее расстояние через вершину k
                d = V[i][k] + V[k][j] # Сумма расстояний от i до k и от k до j
                # Если найден более короткий путь, обновляет матрицу расстояний
                if V[i][j] > d: # Проверяем, меньше ли расстояние d, чем текущее расстояние V[i][j]
                    V[i][j] = d # Обновляем V[i][j] на найденное более короткое расстояние
    # Возвращает обновленную матрицу расстояний               
    return V