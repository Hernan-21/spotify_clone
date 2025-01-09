<script>
  export let categories = [];
</script>

<div class="categories-container">
  <h2>Explorar Categorías</h2>
  <div class="categories-grid">
    {#if categories}
      {#each categories as category}
        <div class="category-card">
          {#if category.icons && category.icons[0]}
            <img src={category.icons[0].url} alt={category.name} class="category-image"/>
          {/if}
          <h3>{category.name}</h3>
        </div>
      {/each}
    {/if}
  </div>
</div>

<style>
  .categories-container {
    padding: 2rem;
  }

  .categories-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 1.5rem;
    margin-top: 1rem;
  }

  .category-card {
    background: linear-gradient(135deg, #450af5, #c4efd9);
    border-radius: 0.5rem;
    padding: 1rem;
    color: white;
    text-align: center;
    transition: transform 0.2s;
    cursor: pointer;
  }

  .category-card:hover {
    transform: scale(1.05);
  }

  .category-image {
    width: 100px;
    height: 100px;
    object-fit: cover;
    margin-bottom: 1rem;
  }

  h3 {
    margin: 0;
    font-size: 1.1rem;
  }
</style> 