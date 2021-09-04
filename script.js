function normalize(num) {
  // shift decimal place so that 0.1 <= num < 1
  var magnitude = Math.floor(Math.log10(num))
  return num / Math.pow(10, magnitude + 1)
}

function hash(secret) {
  var result = 1;
  for (var i = 0; i < secret.length; i++) {
    result *= Math.pow(i+2, secret[i].charCodeAt(0))
    result = normalize(result)
  }
  return result.toString(36).substring(2)
}

var logins = {
  'wp8bsoxhtk': 'ellabc23',
  '864se0jzq2m' : 'oona',
  '4kuv15ffb4q' : 'zahara',
  '53xinoul7yl' : 'isabelle',
  'aokdkdulmn' : 'guest',
  
}

var logged_in_user = logins[hash(prompt('Enter your password'))];

if (logged_in_user) {
  window.location.href='https://ellabc23.github.io/everything.io/home.html';
  alert(`Welcome, ${logged_in_user}`);
} else {
  alert('There is no user with that password. Try again or sign up! If you forgot, contact the owner.')
}





