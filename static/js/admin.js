/* پنل مدیریت: تقویم شمسی روی فیلدهای تاریخ، حتی در inline های تازه اضافه‌شده */
(function () {
  function start() {
    if (!window.jalaliDatepicker) return;
    jalaliDatepicker.startWatch({ persianDigits: true, autoShow: true, autoHide: true, hideAfterChange: true,
      showTodayBtn: true, showEmptyBtn: true, time: false, separatorChar: '/', zIndex: 9999 });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
  /* ارقام فارسی → لاتین قبل از ذخیره */
  document.addEventListener('submit', function (e) {
    var f = e.target; if (!f.querySelectorAll) return;
    f.querySelectorAll('input.jdp, input[data-jdp]').forEach(function (i) {
      i.value = i.value.replace(/[۰-۹]/g, function (d) { return '۰۱۲۳۴۵۶۷۸۹'.indexOf(d); });
    });
  }, true);
})();
