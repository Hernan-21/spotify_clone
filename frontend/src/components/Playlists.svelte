<script>
  export let playlists;
</script>

<div class="playlists-container">
  <h2>Tus Playlists</h2>
  <div class="playlists-grid">
    {#if playlists}
      {#each playlists as playlist}
        <div class="playlist-card">
          {#if playlist.images && playlist.images[0]}
            <img src={playlist.images[0].url} alt={playlist.name} class="playlist-image"/>
          {/if}
          <div class="playlist-info">
            <h3>{playlist.name}</h3>
            <p>{playlist.tracks.total} canciones</p>
          </div>
        </div>
      {/each}
    {/if}
  </div>
</div>

<style>
  .playlists-container {
    padding: 2rem;
  }

  .playlists-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin-top: 1rem;
  }

  .playlist-card {
    background: #282828;
    border-radius: 0.5rem;
    overflow: hidden;
    transition: transform 0.2s;
    cursor: pointer;
  }

  .playlist-card:hover {
    transform: scale(1.05);
  }

  .playlist-image {
    width: 100%;
    aspect-ratio: 1;
    object-fit: cover;
  }

  .playlist-info {
    padding: 1rem;
    color: white;
  }

  .playlist-info h3 {
    margin: 0;
    font-size: 1rem;
  }

  .playlist-info p {
    margin: 0.5rem 0 0;
    opacity: 0.7;
    font-size: 0.9rem;
  }
</style> 