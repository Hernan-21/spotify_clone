<script>
  export let user;
</script>

<div class="profile-container">
  {#if user}
    <div class="profile-header">
      {#if user.images && user.images[0]}
        <img src={user.images[0].url} alt="Profile" class="profile-image"/>
      {/if}
      <div class="profile-info">
        <h1>¡Hola, {user.display_name}!</h1>
        <p>{user.followers.total} seguidores</p>
      </div>
    </div>
  {/if}
</div>

<style>
  .profile-container {
    padding: 2rem;
    background: linear-gradient(to bottom, #1DB954, #191414);
    color: white;
    border-radius: 1rem;
    margin-bottom: 2rem;
  }

  .profile-header {
    display: flex;
    align-items: center;
    gap: 2rem;
  }

  .profile-image {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    border: 3px solid white;
  }

  .profile-info h1 {
    margin: 0;
    font-size: 2.5rem;
  }

  .profile-info p {
    margin: 0.5rem 0;
    opacity: 0.8;
  }
</style> 