$(function () {
    $('.vjDateField').datepicker({
        dateFormat: 'yy-mm-dd',
        changeMonth: true,
        changeYear: true,
        showOn: 'button',
        buttonImage: '/static_back_end/admin/jquery.ui.datepicker.jalali/themes/base/images/icon-calendar.svg',
        buttonImageOnly: true,
        isrtl: true
    });
});
