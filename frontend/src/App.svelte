<script lang="ts">
  import { onMount } from 'svelte';

  // Define the Product type
  // define the product
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
    image_related2: string;
    image_related3: string;
    payment_methods: string[];
    warranty: string;
    description_detail: str;
    product_related: str ;
    price_related: float;
    price_related2: float;
    price_related3: float;
    
  };

  let product: Product | null = null;
  let loading = true;
  let error: string | null = null;


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
   <div class="header-content-rigth">
   <button class="link-button" on:click={handleButtonClick}>
        Vender uno igual</button>/<button class="link-button" on:click={handleButtonClick}>
        Compartir
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
    <p class="product-price">US$ {product.price}<span class="discount">12% off</span></p>
    <p>en <span class="discount">10 cuotas de $ 1.914° sin interés</span></p>
    <div class="seller-info">
      
      <button class="link-button" on:click={handleButtonClick}>
        Ver medio de pago y promociones
        
      </button>
    </div>

    <img src={product.image_url} alt={product.title} class="product-thumbnail" />

    <p>Color: <strong>{product.color}</strong><br/></p>
       <strong>Lo que tienes que saber del producto</strong><br/> 
        <ul>
              <li><strong>Memoria Ram:</strong> {product.memory}</li>
              <li><strong>Memoria Interna:</strong> {product.intern_memory}</li>
            
        </ul>
         <button class="link-button" on:click={handleButtonClick}>
         Ver características
        
      </button>
     
     <p>Opciones de Compra:<br/>
      <button class="link-button" on:click={handleButtonClick}>
       3 productos nuevos desde US$ {product.price}</p>
      

  </div>

  <!-- Columna 3: Acciones -->
  <div class="product-actions-column">
    <div class="product-actions">
      <p><span class="discount">Envío gratis</span> a todo el pais<br/>Conocé los tiempos y formas de pago <br/>
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
       Ver 3 opciones desde US$ {product.price}
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

    <div class="payment-methods">
      <h4>Medios de pago</h4>
      <h3>¡Pagá en hasta <strong>12 cuotas sin <br/>interés!</strong></h3>
      <div class="payment-icons">
        {#each product.payment_methods as method}
          <span class="payment-method-icon">{method}</span>
        {/each}
            </div>
      
      <button class="link-button" on:click={handleButtonClick}>
        Conocer más sobre formas de pago
      </button>
    </div>

  </div>
  
</div>
<section class="related-products">
      <h2 >Productos relacionados</h2>
      <div class="product-grid">
        
        <div class="related-product-card">
          <img src={product.image_related} alt="Related Product 2" />
          <p>{product.product_related}</p>
          <p>US$ {product.price_related}</p>
        </div>
        <div class="related-product-card">
          <img src={product.image_related2} alt="Related Product 3" />
          <p>{product.product_related2}</p>
          <p>US$ {product.price_related2} </p>
        </div>
      </div>
    </section>
   


    <!-- Samsung Products Section (as seen in PDF) -->
    <section class="samsung-products">
      <h2>Productos de Samsung</h2>
      <div class="product-grid">
      
        <div class="samsung-product-card">
          <img src={product.image_related3} alt="Samsung Product 1"/>
          <p>{product.product_related3}</p>
          <p>US$ {product.price_related3}</p>
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

 <!--El etile css se envcuentra en un archivo adjunto llamado app.css -->}
 <!--The CSS style is in an attached file call app.css-->