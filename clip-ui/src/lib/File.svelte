<script>
    let count = 0
    const increment = () => {
      count += 1
    }
  </script>
  
  <div class="right">
    Clicks: {count}
    <span>file name</span>
    <span>file size</span>
  </div>
  
  <style>
    .right {
        margin-left:71%; 
        width:29%;
        background-color: rgba(255, 62, 0, 0.1);
        border: 2px solid rgba(19, 18, 18, 0);
    }
  </style>