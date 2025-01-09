<script>
  import { onMount } from 'svelte';
  import Sidebar from './components/Sidebar.svelte';
  import TopBar from './components/TopBar.svelte';
  import TopTracks from './components/TopTracks.svelte';
  import Playlists from './components/Playlists.svelte';
  import Categories from './components/Categories.svelte';
  import NewReleases from './components/NewReleases.svelte';

  let data = $state(null);
  let error = $state(null);
  let loading = $state(true);

  onMount(async () => {
    try {
      loading = true;
      const response = await fetch('http://localhost:8080/');
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      data = await response.json();
    } catch (e) {
      error = e.message;
      console.error('Error:', e);
    } finally {
      loading = false;
    }
  });
</script>

<div class="app">
  <Sidebar playlists={data?.playlists || []} />
  
  <main class="main-content">
    <TopBar user={data?.user} />
    
    <div class="content">
      {#if loading}
        <div class="loading">Cargando...</div>
      {:else if error}
        <div class="error">Error: {error}</div>
      {:else if data}
        <TopTracks tracks={data.top_tracks} currentTrack={null} />
        <NewReleases releases={data.new_releases} />
        <Categories categories={data.categories} />
        <Playlists playlists={data.playlists} />
      {:else}
        <div>No hay datos disponibles</div>
      {/if}
    </div>
  </main>
</div>

<style>
  :global(body) {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif;
    background-color: #121212;
    color: white;
  }

  .app {
    display: flex;
  }

  .main-content {
    flex-grow: 1;
    margin-left: 240px;
  }

  .content {
    padding: 64px 32px 0;
  }

  .loading, .error {
    text-align: center;
    padding: 2rem;
    font-size: 1.2rem;
  }

  .error {
    color: #ff5555;
  }
</style>
