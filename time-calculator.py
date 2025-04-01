def add_time(start, duration, day=None):
    
    # Analisar a hora de início
    start_time, period = start.split()
    hours, minutes = map(int, start_time.split(':'))
    
    # Converta para o formato de 24 horas para facilitar o cálculo
    if period == 'PM' and hours != 12:
        hours += 12
    elif period == 'AM' and hours == 12:
        hours = 0
    
    # Analisar o tempo de duração
    dur_hours, dur_minutes = map(int, duration.split(':'))
    
    # Adicionando a duração
    total_minutes = minutes + dur_minutes
    added_hours = total_minutes // 60
    remaining_minutes = total_minutes % 60
    
    total_hours = hours + dur_hours + added_hours
    added_days = total_hours // 24
    remaining_hours = total_hours % 24
    
    # Converter de volta para o formato de 12 horas
    if remaining_hours == 0:
        new_hours = 12
        new_period = 'AM'
    elif remaining_hours < 12:
        new_hours = remaining_hours
        new_period = 'AM'
    elif remaining_hours == 12:
        new_hours = 12
        new_period = 'PM'
    else:
        new_hours = remaining_hours - 12
        new_period = 'PM'
    
    # Formata o novo horário
    new_time = f"{new_hours}:{remaining_minutes:02d} {new_period}"
    
    # Identifica o dia da semana, se fornecido
    if day:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        current_day_index = days_of_week.index(day.lower().capitalize())
        new_day_index = (current_day_index + added_days) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"
    
    # Lidar com a mensagem de dias depois
    if added_days == 1:
        new_time += " (next day)"
    elif added_days > 1:
        new_time += f" ({added_days} days later)"
    
    return new_time