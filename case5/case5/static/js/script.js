c = 0
function inf() {
    if (c == 0) {
        a = document.getElementById('inf')
        a.innerHTML = '<h1 class="mt-3">Название мероприятия</h1><h3>Тип мероприятия</h3><p><small>ываывашфвпафвапфшывашщршгрврфщврашпывгашп</small></p><p>Зал</p><h3>Оборудование</h3><p>sdf - 3</p><p>sdf - 3</p><p>sdf - 3</p><p>sdf - 3</p><p>sdf - 3</p><h3>Контактные данные</h3><p>Плюшкина Афанасья Маркеровна</p><p>телефон</p><p>email</p>'
        c = 1
    }
    else if (c == 1) {
        a = document.getElementById('inf')
        a.innerHTML = ''
        c = 0
    }
}
