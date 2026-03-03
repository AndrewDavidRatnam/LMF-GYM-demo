<template>
  <div class="container">
    <div class="card">
      <h2>Join Ultra Fitness</h2>
      
      <!-- HONEYPOT: Invisible to humans. If a bot fills this, the backend rejects it. -->
      <input type="text" v-model="botTrap" class="hidden" tabindex="-1">

      <input v-model="form.name" type="text" placeholder="Name">
      <input v-model="form.phone" type="tel" placeholder="WhatsApp Number">
      
      <select v-model="form.goal">
        <option value="Weight Loss">Weight Loss</option>
        <option value="Muscle Gain">Muscle Gain</option>
      </select>

      <button @click="submit" :disabled="loading">
        {{ loading ? 'Securing...' : 'Book Free Trial' }}
      </button>

      <p v-if="msg" :class="statusClass">{{ msg }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: { name: '', phone: '', goal: 'Weight Loss' },
      botTrap: '', // The honeypot variable
      loading: false,
      msg: '',
      statusClass: ''
    }
  },
  methods: {
    async submit() {
      this.loading = true;
      try {
        // We send the 'botTrap' as 'website' to the backend
        const res = await fetch('https://psychic-guacamole-9pqpw7qrp9wc97r7-5000.app.github.dev/api/enquiry', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ ...this.form, website: this.botTrap })
        });
        const data = await res.json();
        this.msg = data.message;
        this.statusClass = data.status === 'success' ? 'green' : 'red';
      } catch (e) {
        this.msg = "Server Busy/Rate Limited";
      } finally {
        this.loading = false;
      }
    }
  }
}
</script>

<style scoped>
.hidden { display: none; }
.container { background: #121212; height: 100vh; display: flex; align-items: center; justify-content: center; }
.card { background: #1e1e1e; padding: 2rem; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); width: 350px; }
input, select { width: 100%; margin: 10px 0; padding: 12px; background: #2c2c2c; color: white; border: 1px solid #444; border-radius: 6px; }
button { width: 100%; padding: 12px; background: #ff4500; color: white; border: none; font-weight: bold; cursor: pointer; }
.green { color: #00ff88; margin-top: 10px; }
.red { color: #ff4444; margin-top: 10px; }
</style>
