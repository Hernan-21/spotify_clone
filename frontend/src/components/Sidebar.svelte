<script>
  export let playlists = [];
</script>

<aside class="sidebar">
  <div class="logo">
    <img src="/spotify-logo.png" alt="Spotify" />
  </div>

  <nav class="main-nav">
    <ul>
      <li>
        <a href="/" class="nav-item">
          <i class="fas fa-home"></i>
          Inicio
        </a>
      </li>
      <li>
        <a href="/search" class="nav-item">
          <i class="fas fa-search"></i>
          Buscar
        </a>
      </li>
      <li>
        <a href="/library" class="nav-item">
          <i class="fas fa-books"></i>
          Tu biblioteca
        </a>
      </li>
    </ul>
  </nav>

  <div class="playlists-section">
    <h2>Playlists</h2>
    <ul>
      {#each playlists as playlist}
        <li>
          <a href="/playlist/{playlist.id}" class="playlist-item">
            {playlist.name}
          </a>
        </li>
      {/each}
    </ul>
  </div>
</aside>

<style>
  .sidebar {
    width: 240px;
    background-color: #000;
    height: 100vh;
    position: fixed;
    left: 0;
    top: 0;
    padding: 24px 12px;
    color: #b3b3b3;
  }

  .logo {
    padding: 0 12px;
    margin-bottom: 24px;
  }

  .logo img {
    height: 40px;
  }

  .main-nav ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .nav-item {
    display: flex;
    align-items: center;
    padding: 12px;
    color: #b3b3b3;
    text-decoration: none;
    font-weight: 600;
    gap: 16px;
  }

  .nav-item:hover {
    color: white;
  }

  .playlists-section {
    margin-top: 24px;
    padding: 0 12px;
  }

  .playlist-item {
    display: block;
    padding: 8px 0;
    color: #b3b3b3;
    text-decoration: none;
  }

  .playlist-item:hover {
    color: white;
  }
</style> 