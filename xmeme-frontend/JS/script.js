var posts = document.getElementById("posts");
var baseURL = "http://localhost:8000/";
var length;

// Getting data from the server dynamically
const fetchData =  () => {
  fetch(baseURL + "memes")
  .then((response) => response.json())
  .then((data) => {
    for (var i = 0; i < data.length; i++) {
      var h3 = document.createElement("h3");
      h3.innerHTML = data[i]["name"];

      var p = document.createElement("p");
      ss = data[i]["caption"].split(" ");

      for (var j = 0; j < ss.length; j++) {
        if (ss[j][0] === "#") {
          var n = document.createElement("a");
          var na = document.createTextNode(" " + ss[j]);
          n.appendChild(na);
          n.setAttribute(
            "href",
            "http://127.0.0.1:5500/xmeme-frontend/tags.html" + ss[j]
          );
          p.appendChild(n);
        } else {
          p.innerHTML += ss[j] + " ";
        }
      }

      var img = document.createElement("img");
      img.setAttribute("src", data[i]["url"]);
      img.setAttribute("class", "img-fluid posts-img");

      var div = document.createElement("div");
      div.setAttribute("class", "meme-post");
      div.classList.add("shadow-sm");
      div.appendChild(h3);
      div.appendChild(p);
      div.appendChild(img);
      posts.append(div);
    }
    getCurrentCount(i);
  });
}

function getCurrentCount(currCount){
  setInterval(()=>{
    fetch(baseURL+"count/").then(response=>response.json())
    .then(data=>{
      if(data["length"]>currCount){
        document.getElementById("snackbar").style.visibility = "visible"
        document.getElementById("snackbar").innerHTML = `${data["length"]-currCount} New Posts Available`
      }
    })
  },5000)
}

document.getElementById("snackbar").addEventListener("click",()=>{
  location.reload();
})

fetchData()

document.getElementById("submit").addEventListener("click", () => {
  fetch(baseURL + "memes/", {
    method: "POST",
    body: JSON.stringify({
      name: document.getElementById("name").value + "",
      caption: document.getElementById("caption").value + "",
      url: document.getElementById("url").value + "",
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  }).then(() => {
    document.getElementById("name").value = "";
    document.getElementById("caption").value = "";
    document.getElementById("url").value = "";
    location.reload();
  });
});
// Posting data to backend server


document.getElementById("home-click").addEventListener("click",()=>{
    document.getElementById("posts").style.display = "block";
    document.getElementById("upload").style.display = "none";
})

document.getElementById("upload-click").addEventListener("click",()=>{
  document.getElementById("posts").style.display = "none";
  document.getElementById("upload").style.display = "block";
})