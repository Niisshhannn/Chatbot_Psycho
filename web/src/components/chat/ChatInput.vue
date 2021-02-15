<template>
  <div class="chat-input">
    <input
      class="input-inner"
      v-model="inputValue"
      placeholder="Message..."
      autofocus="autofocus"
      @keyup.enter="handleSend"
    />

    <div class="send-button" @click="handleSend">
      <svg
        t="1613283314316"
        viewBox="0 0 1024 1024"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        p-id="1416"
        width="24"
        height="24"
        fill="#8591a8"
      >
        <path
          d="M946.49 554.53c-8.547 18.328-23.104 32.856-40.543 41.596L246.604 928.894c-46.776 22.872-103.222 4.22-126.961-41.596-10.45-22.126-12.569-47.097-5.335-70.393l72.11-234.742c6.602-21.494 26.456-36.165 48.942-36.165h252.363c18.549-0.075 33.717-15.061 34.14-34.13-0.117-18.774-15.098-33.948-34.14-34.13H235.546c-22.575 0-42.486-14.785-49.014-36.396l-71.157-235.579c-14.888-49.133 13.216-101.537 62.947-116.256 23.019-7.236 47.92-5.04 69.348 6.4l658.277 332.768c45.984 23.487 64.49 80.001 40.543 125.855z"
          p-id="1417"
        ></path>
      </svg>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      inputValue: "",
    };
  },
  methods: {
    handleSend() {
      if (!this.inputValue.trim()) return;
      this.$emit("send", this.inputValue.trim());
      this.inputValue = "";
    },
  },
};
</script>

<style scoped>
.chat-input {
  width: 100%;
  height: 52px;
  background-color: #f0f0f0;
  box-sizing: border-box;
  border-top: 1px solid #ccc;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
}

.input-inner {
  flex: 1 1 72%;
  height: 36px;
  border: 1px solid #ccc;
  padding: 0 6px;
  margin-right: 12px;
  border-radius: 5px;
  box-sizing: border-box;
  outline: none;
  font-size: 16px;
}

.input-inner::-webkit-input-placeholder {
  color: #b9b9b9;
}

.send-button {
  cursor: pointer;
}

.send-button svg {
  display: block;
}
</style>
