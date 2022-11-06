// ============================================== slider ======================================

let nexts = document.querySelectorAll(".btn.next");
nexts.forEach((next, index) => {
  next.addEventListener("click", () => {
    const widthItem = document.querySelector(".product_item").offsetWidth;
    document.querySelector(`.from_list${index}`).scrollLeft += widthItem + 20;
  });
});

let prevs = document.querySelectorAll(".btn.prev");
prevs.forEach((prev, index) => {
  prev.addEventListener("click", () => {
    const widthItem = document.querySelector(".product_item").offsetWidth;
    document.querySelector(`.from_list${index}`).scrollLeft -= widthItem + 20;
    console.log(document.querySelector(".from_list1"));
  });
});

// ======================================= search ========================================
let button_search = document.querySelector(".form_serch .btn");
let search = document.querySelector(".search_bind");
button_search.addEventListener("click", () => {
  window.location = `http://127.0.0.1:5000/product?kw=${search.value}`;
});


search.addEventListener('keypress',(e)=>{
  if(e.key == 'Enter'){
  window.location = `http://127.0.0.1:5000/product?kw=${search.value}`;
  }
})


// ============================================== header animation ===========================
let items =document.querySelectorAll('.item')
let nav =document.querySelector('#header')
document.addEventListener('scroll', (event) => {
  if(window.scrollY > 500){
      nav.classList.add('fixed');
  }else{
      nav.classList.remove('fixed');
  }
  items.forEach(item=>{
    if (item.offsetTop - window.scrollY < 900){
      item.classList.add('show')
    }
  })

})




document.querySelector('.nt_nxt1').onclick = function(){
  let lists = document.querySelectorAll('.banner_item-left');
  document.querySelector('.banner_item_slider').appendChild(lists[0]);
}

document.querySelector('.nt_nxt').onclick = function(){
  let lists = document.querySelectorAll('.banner_item-left');
  document.querySelector('.banner_item_slider').prepend(lists[lists.length - 1]);
}

setInterval(()=>{
  let lists = document.querySelectorAll('.banner_item-left');
  document.querySelector('.banner_item_slider').appendChild(lists[0]);
},2000)