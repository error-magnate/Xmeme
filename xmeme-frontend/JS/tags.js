var tagURL =
  "https://xmeme-backend-crio.herokuapp.com/tags/" + location.hash.slice(1);
document.getElementById("tag").innerHTML += location.hash;
fetch(tagURL)
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
            "https://xmeme-frontend-crio.herokuapp.com/tags.html" + ss[j]
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
  });
