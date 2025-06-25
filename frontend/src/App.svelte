<script lang="ts">
  import { onMount } from 'svelte';
  import Counter from './lib/Counter.svelte';

  type Product = {
    id: number;
    title: string;
    description: string;
    price: number;
    stock: number;
    seller: string;
    image_url: string;
    payment_methods: string[];
    warranty: string;
  };

  let products: Product[] = [];

  onMount(async () => {
    const res = await fetch('http://localhost:8000/api/products');
    products = await res.json();
  });
</script>



<main>
  <h1>Productos disponibles</h1>

  {#if products.length > 0}
    {#each products as product}
      <div class="product-card">
        <h2>{product.title}</h2>
        <img src={product.image_url} alt={product.title} />
        <p>{product.description}</p>
        <p><strong>${product.price}</strong> - Stock: {product.stock}</p>
        <p>Vendedor: {product.seller}</p>
        <p>Métodos de pago: {product.payment_methods.join(', ')}</p>
        <p>Garantía: {product.warranty}</p>
      </div>
    {/each}
  {:else}
    <p>Cargando productos...</p>
  {/if}
</main>

<style>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
  .read-the-docs {
    color: #888;
  }
</style>
