/* Copy account URL to clipboard */
function copyToClipboard() {
  var copyText = document.getElementById("accountUrl");

  copyText.select();
  copyText.setSelectionRange(0, 99999);
}
