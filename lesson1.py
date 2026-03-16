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

def check_loss(loss):
    if loss < 0.2:
        return "Отличный результат"
    elif loss < 0.5:
        return "Хороший результат"
    else:
        return "Нужно продолжить обучение"
    
print(check_loss(0.1))
print(check_loss(0.3))
print(check_loss(0.6))


def training_loop(epochs):
    for epoch in range(1, epochs + 1):
        loss = 1.0 / epoch
        status = check_loss(loss)
        print(f"Эпоха {epoch} из {epochs} | Loss: {loss:.4f} | {status}")
    return "Обучение завершено."

def check_loss(loss):
    if loss < 0.2:
        return "Отличный результат"
    elif loss < 0.5:
        return "Хороший результат"
    else:
        return "Нужно продолжить обучение"

print(training_loop(5))