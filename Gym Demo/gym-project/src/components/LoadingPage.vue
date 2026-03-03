<template>
  <div class="loading-screen">
    <div class="logo-container">
      <div class="spinner"></div>
      <h1 class="glitch">LMF<span>GYM</span></h1>
      <p class="status-text">{{ status }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const status = ref('Every great journey begins with a single step');

onMounted(() => {
  setTimeout(() => { status.value = 'But we also SOTA treadmills lmao'; }, 2000);
  setTimeout(() => {
    router.push('/join'); // This directs to your secure form
  }, 3000);
});
</script>

<style scoped>
.loading-screen {
  background: #000; height: 100vh; display: flex; 
  align-items: center; justify-content: center; color: white;
}
.spinner {
  width: 50px; height: 50px; border: 3px solid rgba(255, 69, 0, 0.2);
  border-top-color: #ff4500; border-radius: 50%;
  animation: spin 1s ease-in-out infinite; margin: 0 auto 20px;
}
.glitch { font-size: 2.5rem; letter-spacing: 5px; font-weight: 900; }
.glitch span { color: #ff4500; }
.status-text { color: #666; font-family: monospace; font-size: 0.9rem; }

@keyframes spin { to { transform: rotate(360deg); } }
</style>
