var run_btn = document.getElementById("run");
run_btn.addEventListener("click", function () {
  var elem = document.querySelector('.modal');
  var instance = M.Modal.init(elem);
  instance.open();
});