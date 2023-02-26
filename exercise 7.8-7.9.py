"""
Создайте список с элементами "Groucho", "Chico" и "Harpo"; назовите его
surprise.
"""

surprise =['Groucho', 'Chico', 'Harpo']

"""
Напишите последний элемент списка surprise со строчной буквы,
затем выведите эту строку в обратном порядке и с прописной буквы.
"""

element = surprise.pop().lower()
print(element)
print(element[::-1].title())