<script lang="ts">
  import { onMount } from 'svelte';

  // Define the Product type
  type Product = {
    id: number;
    title: string;
    description: string;
    old_price: float
    price: number;
    stock: number;
    brand: str;
    color: str;
    seller: string;
    image_url: string;
    image_related: string;
    payment_methods: string[];
    warranty: string;
    description_detail: str;
  };

  let product: Product | null = null;
  let loading = true;
  let error: string | null = null;

  // For this standalone App.svelte, we'll fetch a specific product, e.g., product with ID 1.
  // If you need to switch between products, you'd need client-side routing.
  const productId = 1; // Hardcode product ID for demonstration as per your products.json

  onMount(async () => {
    try {
      // Adjust the fetch URL to get a single product by ID
      const res = await fetch(`http://localhost:8000/api/products/${productId}`);
      if (!res.ok) {
        throw new Error(`Error fetching product: ${res.statusText}`);
      }
      product = await res.json();
    } catch (err: any) {
      error = err.message;
    } finally {
      loading = false;
    }
  });

  // Placeholder function for button clicks
  function handleButtonClick(event: MouseEvent) {
    console.log(`Button clicked: ${(event.target as HTMLElement).textContent}`);
    // In a real application, you'd implement navigation or other actions here.
  }
</script>
<header class="main-header">
  <div class="header-content">
   <button class="link-button" on:click={handleButtonClick}>
        Volver al listado</button>/<button class="link-button" on:click={handleButtonClick}>
        Celulares y Telefonía</button>><button class="link-button" on:click={handleButtonClick}>
        Celulares y Smartphones</button>><button class="link-button" on:click={handleButtonClick}>
        Samsung</button> 
  </div>
</header>

<main>
  {#if loading}
    <p>Cargando producto...</p>
  {:else if error}
    <p class="error">Error: {error}</p>
  {:else if product}
    <div class="product-detail-container">
  <!-- Columna 1: Imagen -->
  <div class="product-images">
    <img src={product.image_url} alt={product.title} class="main-image" />
  </div>

  <!-- Columna 2: Información -->
  <div class="product-info">
    <button class="link-button" on:click={handleButtonClick}>
      Visita la {product.seller}
    </button>
    <h1 class="product-title">{product.title}</h1>

    {#if product.old_price}
      <p class="old-price">US$ {product.old_price}</p>
    {/if}
    <p class="product-price">US$ {product.price}</p>
    
    <div class="seller-info">
      <p>Vendido por: <strong>{product.seller}</strong></p>
      <button class="link-button" on:click={handleButtonClick}>
        Ver medio de pago y promociones
        
      </button>
    </div>

    <div class="payment-methods">
      <h3>Métodos de pago</h3>
      <div class="payment-icons">
        {#each product.payment_methods as method}
          <span class="payment-method-icon">{method}</span>
        {/each}
      </div>
      <button class="link-button" on:click={handleButtonClick}>
        Conocer más sobre formas de pago
      </button>
    </div>
    <p>Color: <strong>{product.color}</strong><br/>
       <strong>Lo que tienes que saber del producto</strong><br/> </p> 
        <ul>
              <li><strong>Memoria Ram:</strong> {product.memory}</li>
              <li><strong>Memoria Interna:</strong> {product.intern_memory}</li>
            
        </ul>
         <button class="link-button" on:click={handleButtonClick}>
         Ver características
        
      </button>
  </div>

  <!-- Columna 3: Acciones -->
  <div class="product-actions-column">
    <div class="product-actions">
      <p>Envío gratis a todo el pais<br/>Conocé los tiempos y formas de pago <br/>
       <button class="link-button" on:click={handleButtonClick}>
        Calcular cuando llega
      </button>
          </p>
      {#if product.stock > 0}
      <p><strong>Stock disponible</strong></p>
    {:else}
      <p><strong>Sin stock</strong></p>
    {/if}

      <button class="buy-now-button">Comprar ahora</button>
      <button class="add-to-cart-button">Agregar al carrito</button>
      <p class="product-actions-p">Tienda: {product.seller}<br/><strong>+5mil ventas</strong><br/>
      <button class="link-button" on:click={handleButtonClick}>
        Devoluvión gratis</button> Tienes 30 días desde que lo recibes.<br/>
        <button class="link-button" on:click={handleButtonClick}>
        Compra protegida</button> Recibe el producto que esperabas o te devolvemos tu dinero.<br/>
        1 año de garantía de fábrica  
      </p>
      
    </div>
     <div class="info-store">
      <p><strong>{product.brand}</strong><br/>
      <strong>{product.seller}</strong><br/>
       <button class="link-button" on:click={handleButtonClick}>
       Ver 3 opciones desde {product.price}
      </button>
          </p>
              
    </div>
    <div class="options-buy">
      <p><strong>Otras opciones de compra </strong><br/>
       <button class="link-button" on:click={handleButtonClick}>
       Ver 3 opciones desde {product.price}
      </button>
          </p>
              
    </div>
    
  </div>
  
</div>

    <!-- Related Products Section (as seen in PDF) -->
    <section class="related-products">
      <h2 >Productos relacionados</h2>
      <div class="product-grid">
        <!-- You'd fetch and loop through related products here -->
        <!-- For now, placeholder divs -->
        <div class="related-product-card">
          <img src={product.image_related} alt="Related Product 1" />
          <p>Producto relacionado 1</p>
          <p>US$ XXX</p>
        </div>
        <div class="related-product-card">
          <img src="/static/img/placeholder.jpg" alt="Related Product 2" />
          <p>Producto relacionado 2</p>
          <p>US$ YYY</p>
        </div>
      </div>
    </section>

    <!-- Samsung Products Section (as seen in PDF) -->
    <section class="samsung-products">
      <h2>Productos de Samsung</h2>
      <div class="product-grid">
        <!-- You'd fetch and loop through other Samsung products here -->
        <!-- For now, placeholder divs -->
        <div class="samsung-product-card">
          <img src="/static/img/placeholder.jpg" alt="Samsung Product 1" />
          <p>Producto Samsung 1</p>
          <p>US$ ZZZ</p>
        </div>
      </div>
    </section>
    <div class="additional-details">
          <h3>Características del producto</h3>
            <ul>
              <li><strong>Descripción:</strong> {product.description}</li>
              <li><strong>Stock disponible:</strong> {product.stock} unidades</li>
              <li><strong>Garantía:</strong> {product.warranty}</li>
              
            </ul>
    </div>
    <section class="description-details-section">
    <div class="description-details">
          <h3>Descripción</h3>
             <p class="product-description-details">{product.description_detail}</p>
    </div>
     </section>
  {:else}
    <p>Producto no encontrado.</p>
  {/if}
</main>

<style>
  /* Set the background color of the body to white for the entire page */
  body {
    background-color: white;
  }
  .main-header {
  background-color:rgb(235, 233, 224);
  padding: 12px 24px;
  display: flex;
  align-items: center;
  border-bottom: 1px solid #ddd;
}
 
p, ul,  li{
  text-align: left;

  color: #333;
}


.header-content {
  display: flex;
  align-items: center;
  gap: 12px;
}


.main-header h1 {
  margin: 0;
  font-size: 20px;
  color: #333;
}

.old-price {
  font-size: 20px;
  color: #999;
  text-decoration: line-through;
  margin-bottom: 5px;
}

.product-detail-container {
  display: grid;
  grid-template-columns: 1fr 1.2fr 0.8fr;
  gap: 30px;
  align-items: start;
  max-width: 1200px;
  width: 100%;
  background-color: white;

}
  
  /* General Layout */
  main {
    font-family: sans-serif;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    background-color: white; /* Ensure main content area is also white */
  }

  .product-detail-container {
    display: flex;
    gap: 40px;
    margin-bottom: 40px;
  }

  .product-images {
    flex: 0 0 40%; /* Adjust as needed */
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .main-image {
    width: 100%;
    max-width: 400px; /* Example max-width */
    height: auto;
    border: 1px solid #eee;
    border-radius: 4px;
  }

  .product-info {
    flex: 1;
  }

  /* Product Info Styling */
  .product-title {
    font-size: 28px;
    font-weight: 500;
    margin-bottom: 10px;
    color: #333;
  }

  .product-price {
    font-size: 36px;
    font-weight: 600;
    color: #333;
    margin-bottom: 20px;
  }
  
  

  .seller-info {
    border-bottom: 1px solid #eee;
    padding-bottom: 15px;
    margin-bottom: 20px;
  }

  .seller-info p {
    margin: 5px 0;
    font-size: 14px;
    color: #666;
  }

  /* Styling for the new link-button */
  .link-button {
    background: none;
    border: none;
    padding: 0;
    color: #3483fa; /* MercadoLibre blue */
    text-decoration: none;
    font-size: 14px;
    cursor: pointer;
    text-align: left; /* Align text to the left like a link */
  }

  .link-button:hover {
    text-decoration: underline;
  }

  .payment-methods h3 {
    font-size: 16px;
    margin-bottom: 10px;
    color: #333;
  }

  .payment-icons {
    display: flex;
    gap: 15px;
    margin-bottom: 10px;
  }

  .payment-method-icon {
    /* Placeholder for actual payment method logos */
    padding: 5px 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 12px;
    color: #555;
    background-color: #f9f9f9;
  }

  /* Removed unused CSS for .payment-methods a and .payment-methods a:hover */

  .product-actions  {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 30px;
    margin-bottom: 30px;
    border: 2px solid #999;
    border-radius: 8px;
    padding: 16px; 
    max-width: 300px;
    width: 100%;

  }
  .product-actions-p{
    color:  #999;
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 30px;
    margin-bottom: 30px;
  }
  .options-buy  {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 30px;
    margin-bottom: 30px;
    border: 2px solid #999;
    border-radius: 8px;
    padding: 16px; 
    max-width: 300px;
    width: 100%;

  }
  .info-store  {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 30px;
    margin-bottom: 30px;
    border: 2px solid #999;
    border-radius: 8px;
    padding: 16px; 
    max-width: 300px;
    width: 100%;

  }

  .buy-now-button,
  .add-to-cart-button {
    padding: 12px 20px;
    border: none;
    border-radius: 6px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.2s;
  }

  .buy-now-button {
    background-color: #3483fa; /* MercadoLibre blue */
    color: white;
  }

  .buy-now-button:hover {
    background-color: #2968c8;
  }

  .add-to-cart-button {
    background-color: #e3e3e3;
    color: #333;
    border: 1px solid #ccc;
  }

  .add-to-cart-button:hover {
    background-color: #d4d4d4;
  }

  .additional-details h3 {
    font-size: 18px;
    margin-bottom: 15px;
    color: #333;
  }

  .additional-details ul {
    list-style: none;
    padding: 0;
  }

  .additional-details ul li {
    margin-bottom: 8px;
    font-size: 15px;
    color: #555;
  }
  
  .description-details {
    font-size: 18px;
    margin-bottom: 15px;
    color: #333;
  }
  .description-details p h3{
    font-size: 18px;
    margin-bottom: 15px;
    color: #333;
  }
  
  .description-details-section {
    margin-top: 40px;
    border-top: 1px solid #eee;
    padding-top: 30px;
  }

  /* Related Products and Samsung Products Sections */
  .related-products,
  .samsung-products {
    margin-top: 40px;
    border-top: 1px solid #eee;
    padding-top: 30px;
  }

  .related-products h2,
  .samsung-products h2 {
    font-size: 20px;
    font-weight: 500;
    margin-bottom: 20px;
    color: #333;
  }

  .product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 20px;
  }

  .related-product-card,
  .samsung-product-card {
    border: 1px solid #eee;
    border-radius: 8px;
    padding: 15px;
    text-align: center;
    background-color: #fff;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
  }

  .related-product-card img,
  .samsung-product-card img {
    max-width: 100%;
    height: 120px; /* Fixed height for consistency */
    object-fit: contain; /* Ensures the image fits without distortion */
    margin-bottom: 10px;
  }

  .related-product-card p,
  .samsung-product-card p {
    margin: 5px 0;
    font-size: 14px;
    color: #333;
  }

  .related-product-card p:last-child,
  .samsung-product-card p:last-child {
    font-weight: 600;
    font-size: 16px;
  }

  /* Responsive Adjustments */
  @media (max-width: 768px) {
    .product-detail-container {
      flex-direction: column;
      gap: 20px;
    }

    .product-images {
      width: 100%;
    }
  }

  .error {
    color: red;
    font-weight: bold;
  }
</style>
