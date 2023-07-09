// popup login
document.querySelector("#show-login").addEventListener("click", function () {
  document.querySelector(".popup").classList.add("active");
});
document.querySelector(".popup .close-btn").addEventListener("click", function () {
  document.querySelector(".popup").classList.remove("active");
});

// selamat datang
// fungsi tombol daftar
document.querySelector('.form-element button').addEventListener('click', function () {
  // jika id email & password terisi (lebih dari 1 karakter), maka tersimpan di cookie + web reload
  if (document.querySelector('#email').value.length > 0 && document.querySelector('#password').value.length > 0)
      document.cookie = 'yes'
  if (document.querySelector('#email').value.length > 0 && document.querySelector('#password').value.length > 0)
      location.reload();
});
// jika terdapat cookie, maka <a></a> dengan id show-login diganti dengan "Selamat Datang"
if (document.cookie == 'yes') {
  document.querySelector('a#show-login').textContent = "Selamat Datang"
};
// fungsi tombol log out
// mereset cookie jika tersedia, kemudian reload page
document.querySelector('.tombol').addEventListener('click', function () {
  document.cookie = 'no'
  location.reload();
});