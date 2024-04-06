document.getElementById("myForm").addEventListener("submit", function(event) {
  event.preventDefault();
  const Name = document.getElementById("Name").value;
  const lastName = document.getElementById("lastName").value;
  const jsonData = {
    Name: Name,
    lastName: lastName
  };
  const jsonString = JSON.stringify(jsonData);
  document.getElementById("output").innerText = jsonString;
});

