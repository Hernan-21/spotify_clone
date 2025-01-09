<script lang="ts">
  interface Artist {
    name: string;
  }

  interface Album {
    images: { url: string }[];
  }

  interface Track {
    id: string;
    name: string;
    album: Album;
    artists: Artist[];
    preview_url?: string;
  }

  let { currentTrack } = $props<{ currentTrack: Track | null }>();
  let isPlaying = $state(false);
  let volume = $state(1);
  let audio: HTMLAudioElement;

  $effect(() => {
    if (currentTrack?.preview_url && audio) {
      audio.src = currentTrack.preview_url;
      if (isPlaying) {
        audio.play();
      }
    }
  });

  function togglePlay() {
    if (!audio) return;
    
    if (isPlaying) {
      audio.pause();
    } else {
      audio.play();
    }
    isPlaying = !isPlaying;
  }

  function handleVolumeChange(e: MouseEvent | KeyboardEvent) {
    const slider = e.currentTarget as HTMLDivElement;
    const rect = slider.getBoundingClientRect();
    
    let newVolume: number;
    if (e instanceof KeyboardEvent) {
      // Arrow keys adjust volume by 10%
      if (e.key === 'ArrowRight') newVolume = Math.min(1, volume + 0.1);
      else if (e.key === 'ArrowLeft') newVolume = Math.max(0, volume - 0.1);
      else return;
    } else {
      const x = e.clientX - rect.left;
      newVolume = Math.max(0, Math.min(1, x / rect.width));
    }
    
    volume = newVolume;
    if (audio) audio.volume = volume;
  }
</script>

<audio 
  bind:this={audio}
  onended={() => isPlaying = false}
></audio>

<div class="player">
  <div class="now-playing">
    {#if currentTrack}
      <img src={currentTrack.album.images[0].url} alt={currentTrack.name} class="track-image"/>
      <div class="track-info">
        <div class="track-name">{currentTrack.name}</div>
        <div class="artist-name">{currentTrack.artists[0].name}</div>
      </div>
    {/if}
  </div>

  <div class="player-controls">
    <button class="control-button" aria-label="Aleatorio">
      <i class="fas fa-random"></i>
    </button>
    <button class="control-button" aria-label="Anterior">
      <i class="fas fa-step-backward"></i>
    </button>
    <!-- svelte-ignore event_directive_deprecated -->
    <button 
      class="control-button play" 
      aria-label={isPlaying ? 'Pausar' : 'Reproducir'}
      onclick={togglePlay}
    >
      <i class="fas {isPlaying ? 'fa-pause' : 'fa-play'}"></i>
    </button>
    <button class="control-button" aria-label="Siguiente">
      <i class="fas fa-step-forward"></i>
    </button>
    <button class="control-button" aria-label="Repetir">
      <i class="fas fa-redo"></i>
    </button>
  </div>

  <div class="volume-control">
    <i class="fas fa-volume-up"></i>

    <div 
      class="volume-slider" 
      role="slider" 
      aria-label="Control de volumen"
      aria-valuenow={Math.round(volume * 100)}
      aria-valuemin="0"
      aria-valuemax="100"
      tabindex="0"
      onclick={handleVolumeChange}
      onkeydown={handleVolumeChange}
    >
      <div 
        class="volume-progress"
        style="width: {volume * 100}%"
      ></div>
    </div>
  </div>
</div>

<style>
  .player {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    height: 90px;
    background: #181818;
    border-top: 1px solid #282828;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 16px;
    z-index: 100;
  }

  .now-playing {
    display: flex;
    align-items: center;
    min-width: 180px;
    width: 30%;
  }

  .track-image {
    width: 56px;
    height: 56px;
    margin-right: 14px;
  }

  .track-info {
    display: flex;
    flex-direction: column;
  }

  .track-name {
    color: white;
    font-size: 14px;
    margin-bottom: 4px;
  }

  .artist-name {
    color: #b3b3b3;
    font-size: 12px;
  }

  .player-controls {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 16px;
    flex: 1;
  }

  .control-button {
    background: none;
    border: none;
    color: #b3b3b3;
    cursor: pointer;
    padding: 8px;
    border-radius: 50%;
  }

  .control-button:hover {
    color: white;
  }

  .control-button.play {
    background: white;
    color: black;
    width: 32px;
    height: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .control-button.play:hover {
    transform: scale(1.1);
  }

  .volume-control {
    display: flex;
    align-items: center;
    gap: 8px;
    min-width: 180px;
    width: 30%;
    justify-content: flex-end;
  }

  .volume-slider {
    width: 100px;
    height: 4px;
    background: #4f4f4f;
    border-radius: 2px;
    position: relative;
    cursor: pointer;
  }

  .volume-progress {
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 50%;
    background: #b3b3b3;
    border-radius: 2px;
  }

  .volume-slider:hover .volume-progress {
    background: #1db954;
  }
</style> 