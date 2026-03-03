<template>
  <div class="home-page">
    <nav class="navbar">
      <div class="logo">LMF<span>GYM</span></div>
      <div class="nav-links">
        <a href="#about">About</a>
        <a href="#plans">Plans</a>
        <button @click="startOnboarding" class="contact-btn">CONTACT US</button>
      </div>
    </nav>

    <section class="hero-section">
      <div class="hero-content">
        <h2 class="reveal">STOP WAITING.</h2>
        <h1 class="glitch-text">START FORGING.</h1>
        <p>Advanced Data-Driven Training for the 1%.</p>
        <button @click="startOnboarding" class="cta-main">JOIN THE TRIBE</button>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
const router = useRouter();

const startOnboarding = () => {
  // Direct to loading first, then the form
  router.push('/loading');
};
</script>

<style scoped>
.home-page { background: #000; color: white; min-height: 100vh; font-family: 'Inter', sans-serif; }
.navbar { display: flex; justify-content: space-between; padding: 30px 10%; align-items: center; }
.logo { font-size: 1.8rem; font-weight: 900; letter-spacing: 2px; }
.logo span { color: #ff4500; }
.contact-btn { background: transparent; border: 1px solid #ff4500; color: #ff4500; padding: 10px 20px; cursor: pointer; transition: 0.3s; }
.contact-btn:hover { background: #ff4500; color: white; }

.hero-section { height: 80vh; display: flex; align-items: center; justify-content: center; text-align: center; }
.hero-content h2 { color: #666; letter-spacing: 5px; margin-bottom: 0; }
.hero-content h1 { font-size: 5rem; margin-top: 0; font-weight: 900; }
.cta-main { background: #ff4500; color: white; border: none; padding: 20px 40px; font-size: 1.2rem; font-weight: bold; cursor: pointer; box-shadow: 0 10px 20px rgba(255, 69, 0, 0.3); }
</style>
