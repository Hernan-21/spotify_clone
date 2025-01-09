<script>
  export let tracks;
</script>

<div class="tracks-container">
  <h2>Tus Top Tracks</h2>
  <div class="tracks-grid">
    {#if tracks}
      {#each tracks as track}
        <div class="track-card">
          {#if track.album.images && track.album.images[0]}
            <img src={track.album.images[0].url} alt={track.name} class="track-image"/>
          {/if}
          <div class="track-info">
            <h3>{track.name}</h3>
            <p>{track.artists.map(artist => artist.name).join(', ')}</p>
          </div>
          <iframe
            src="https://open.spotify.com/embed/track/{track.id}"
            width="100%"
            height="80"
            frameBorder="0"
            allowTransparency={true}
            allow="encrypted-media"
            title={`Play ${track.name} by ${track.artists[0].name}`}
          ></iframe>
        </div>
      {/each}
    {/if}
  </div>
</div>

<style>
  .tracks-container {
    padding: 2rem;
  }

  .tracks-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 1rem;
  }

  .track-card {
    background: #282828;
    border-radius: 0.5rem;
    padding: 1rem;
    color: white;
    transition: transform 0.2s;
  }

  .track-card:hover {
    transform: translateY(-5px);
  }

  .track-image {
    width: 100%;
    aspect-ratio: 1;
    object-fit: cover;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
  }

  .track-info {
    margin-bottom: 1rem;
  }

  .track-info h3 {
    margin: 0;
    font-size: 1.2rem;
  }

  .track-info p {
    margin: 0.5rem 0;
    opacity: 0.7;
  }
</style> 