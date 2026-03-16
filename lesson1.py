def greeting(name):
    return f"Привет, {name}! Ты будешь ИИ разработчиком."
    

print(greeting("Артем"))

def add(a, b):
   return a + b

print(add(5, 3))


def describe_model(name, accuracy):
    return f"Модель {name} имеет точность {accuracy}%."

print(describe_model("GPT", 95))


def training_loop(epochs):
    for epoch in range(1, epochs + 1):
        print(f"Эпоха {epoch} из {epochs}")
    return "Обучение завершено."

print(training_loop(5))

def training_loop(epochs):
    for epoch in range(1, epochs + 1):
        loss = 1.0 / epoch  # потеря уменьшается с каждой эпохой
        print(f"Эпоха {epoch} из {epochs} | Loss: {loss:.4f}")
    return "Обучение завершено."
print(training_loop(5))