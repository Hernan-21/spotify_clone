<script>
  export let releases = [];
</script>

<div class="releases-container">
  <h2>Nuevos Lanzamientos</h2>
  <div class="releases-grid">
    {#if releases}
      {#each releases as album}
        <div class="release-card">
          {#if album.images && album.images[0]}
            <img src={album.images[0].url} alt={album.name} class="release-image"/>
          {/if}
          <div class="release-info">
            <h3>{album.name}</h3>
            <p>{album.artists.map(artist => artist.name).join(', ')}</p>
          </div>
        </div>
      {/each}
    {/if}
  </div>
</div>

<style>
  .releases-container {
    padding: 2rem;
  }

  .releases-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1.5rem;
    margin-top: 1rem;
  }

  .release-card {
    background: #282828;
    border-radius: 0.5rem;
    overflow: hidden;
    transition: transform 0.2s;
    cursor: pointer;
  }

  .release-card:hover {
    transform: scale(1.05);
  }

  .release-image {
    width: 100%;
    aspect-ratio: 1;
    object-fit: cover;
  }

  .release-info {
    padding: 1rem;
    color: white;
  }

  .release-info h3 {
    margin: 0;
    font-size: 1.1rem;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .release-info p {
    margin: 0.5rem 0 0;
    opacity: 0.7;
    font-size: 0.9rem;
  }
</style> 