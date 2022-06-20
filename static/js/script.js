$(document).ready(function () {

  $('.modal').modal();
  $('#textarea1').val('');
  $('input#input_text, textarea#content').characterCounter();
  M.textareaAutoResize($('#content'));
  $('select').formSelect();
  $('.datepicker').datepicker({
    format: "dd mmmm,yyyy",
    yearRange: 3,
    showClearBtn: true,
    i18n: {
      done: "Select"
    }
  })
})