<script>
  export let user;
</script>

<header class="topbar">
  <div class="navigation-buttons">
    <!-- svelte-ignore a11y_consider_explicit_label -->
    <button class="nav-button">
      <i class="fas fa-chevron-left"></i>
    </button>
    <!-- svelte-ignore a11y_consider_explicit_label -->
    <button class="nav-button">
      <i class="fas fa-chevron-right"></i>
    </button>
  </div>

  <div class="search-bar">
    <i class="fas fa-search"></i>
    <input type="text" placeholder="¿Qué quieres reproducir?" />
  </div>

  <div class="user-menu">
    {#if user}
      <button class="user-button">
        {#if user.images && user.images[0]}
          <img src={user.images[0].url} alt={user.display_name} />
        {:else}
          <i class="fas fa-user"></i>
        {/if}
        {user.display_name}
      </button>
    {/if}
  </div>
</header>

<style>
  .topbar {
    height: 64px;
    background-color: rgba(0, 0, 0, 0.7);
    display: flex;
    align-items: center;
    padding: 0 32px;
    position: fixed;
    top: 0;
    right: 0;
    left: 240px;
    z-index: 100;
  }

  .navigation-buttons {
    display: flex;
    gap: 16px;
  }

  .nav-button {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background-color: rgba(0, 0, 0, 0.7);
    border: none;
    color: white;
    cursor: pointer;
  }

  .search-bar {
    margin-left: 32px;
    position: relative;
    flex-grow: 1;
    max-width: 364px;
  }

  .search-bar input {
    width: 100%;
    height: 40px;
    border-radius: 20px;
    border: none;
    padding: 0 40px;
    background-color: white;
  }

  .search-bar i {
    position: absolute;
    left: 12px;
    top: 50%;
    transform: translateY(-50%);
    color: #121212;
  }

  .user-menu {
    margin-left: auto;
  }

  .user-button {
    display: flex;
    align-items: center;
    gap: 8px;
    background: rgba(0, 0, 0, 0.7);
    border: none;
    color: white;
    padding: 2px 8px;
    border-radius: 23px;
    cursor: pointer;
  }

  .user-button img {
    width: 28px;
    height: 28px;
    border-radius: 50%;
  }
</style> 