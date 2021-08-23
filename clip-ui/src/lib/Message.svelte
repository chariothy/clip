<script>
  let count = 0
  const increment = () => {
    count += 1
  }
</script>

<div class="left">
  Clicks: {count}
  <textarea></textarea>
</div>

<style>
  .left {
    float: left;
    width: 70%;
    background-color: rgba(255, 62, 0, 0.1);
    border: 2px solid rgba(19, 18, 18, 0);
  }
</style>
