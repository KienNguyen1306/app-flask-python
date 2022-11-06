// ========================== add cart===============================

function add_cart(id, name, des, price, image) {
  // event.preventDefault();
  fetch("/api/in-cart", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      id: id,
      name: name,
      des: des,
      price: price,
      image: image,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
      document.querySelector(".count").innerHTML = data.sum_count;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

// ================================================== update cart ===========================
function update_cart(id, obj, price) {
  event.preventDefault();
  fetch("/api/update-cart", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      id: id,
      count: obj.value,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
      document.querySelector(".count").innerHTML = data.sum_count;
      document.querySelector(".count1").innerHTML = data.sum_count;
      document.querySelector(`.col_count_${id}`).innerText =
        String(obj.value * price).replace(/\B(?=(\d{3})+(?!\d))/g, ",") + "VND";
      document.querySelector(".sum_price").innerText =
        String(data.sum_price).replace(/\B(?=(\d{3})+(?!\d))/g, ",") + "VND";
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

// ====================================================== delete product ==========================
function delete_cart(id) {
  event.preventDefault();
  if (confirm("Bạn có muốn xóa không ") == true) {
    fetch("/api/delete/" + id, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
        document.querySelector(".count").innerText = data.sum_count;
        document.querySelector(".count1").innerText = data.sum_count;

        document.querySelector(`.product_${id}`).style.display = "none";

        document.querySelector(".sum_price").innerText =
          String(data.sum_price).replace(/\B(?=(\d{3})+(?!\d))/g, ",") + "VND";
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
}

// ====================================== pay ===========================
function pay() {
  if (confirm("Bạn có muốn thanh toán ") == true) {
    fetch("/api/pay", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
        if (data.code == 200) {
          location.reload();
          alert("Thanh toán thành công");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
}

// ========================================================= add comment =================================

function add_comment(product_id) {
  const comment = document.querySelector(".textarea");
  fetch("/api/comment", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      product_id: product_id,
      content: comment.value,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
      const comment_body = document.querySelector(
        ".product_detail_comment-content"
      );
      comment_body.innerHTML =
        `
                  <div class="product_detail_comment_list">
                    <div class="product_detail_comment_list_left">
                      <img src="${data.user.avatar}" alt="" />
                    </div>
                    <div class="product_detail_comment_list_right">
                      <h4>${data.user.name}</h4>
                      <p class="comment_time">${moment( data.data.create_time).fromNow()}</p>
                      <p class="comment_content">${data.data.content}</p>
                    </div>
                  </div>
      ` + comment_body.innerHTML;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

window.onload = () => {
  let time_data = document.querySelectorAll(".date.text-black-50");
  time_data.forEach((data) => {
    data.innerText = moment(data.innerText).fromNow();
  });

  

  // ============================================== load mỏe ==================================
  // let items = document.querySelectorAll(".item_comment");
  // var page = 1;
  // var size = 4;
  // let start = 0;
  // let end = size * page - 1;
  // function load_item() {
  //   items.forEach((item, index) => {
  //     if (index >= start && index < end) {
  //       item.style.display = "block";
  //     } else {
  //       item.style.display = "none";
  //     }
  //   });
  // }
  // load_item();

  // document.querySelector(".load_more").addEventListener("click", () => {
  //   end += size;
  //   load_item();
  // });
};
