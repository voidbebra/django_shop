$(document).ready(function() {
    // Обработчик клика на кнопке "Add to cart"
    $(".updateForm .btn-outline-dark").click(function(event) {
      event.preventDefault(); // Предотвратить стандартное действие кнопки
  
      // Находим родительскую форму и выполняем AJAX-запрос
      var form = $(this).closest(".updateForm");
      var formData = form.serialize(); // Получить данные формы
  
      // Ваш код для обработки данных, например, отправка AJAX-запроса
      $.ajax({
        type: 'POST',
        url: form.attr('action'),
        data: formData,
        dataType: 'json',
        success: function(data) {
          // Обработка успешного ответа от сервера
          console.log(data);
  
          if (data.success) {
            // Здесь можно выполнить дополнительные действия после успешного ответа
            console.log("Успешно добавлено в корзину.");
          } else {
            console.log("Произошла ошибка при добавлении в корзину.");
          }
        },
        error: function(xhr, status, error) {
          // Обработка ошибки запроса
          console.log("Произошла ошибка при отправке запроса.");
          console.log(error);
        }
      });
      // Предотвратить всплытие события, чтобы избежать перенаправления при клике на .card
      event.stopPropagation();
    });
});
    // Обработчик клика на карточке товара
    const product_detail = (url) => {
      window.location.href = url;
    };
  