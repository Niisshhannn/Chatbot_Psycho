<template>
  <div class="chat-option">
    <div
      v-for="opt in options"
      :key="opt.key"
      class="opt-item"
      @click="handleClick(opt)"
    >
      {{ opt.value }}
    </div>
  </div>
</template>

<script>
export default {
  props: {
    options: {
      type: Array,
      default: () => [],
    },
  },
  methods: {
    handleClick(item) {
      this.$emit("choose", item);
    },
  },
};
</script>

<style scoped>
.chat-option {
  width: 70%;
  display: flex;
  box-sizing: border-box;
  padding: 0 8px 10px;
  margin: 0 auto;
  justify-content: space-around;
}

.opt-item {
  line-height: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 4px;
  background-color: #1965ff;
  padding: 6px 12px;
  color: #fff;
  box-shadow: 0 0 10px rgb(0 0 0 / 15%);
  cursor: pointer;
}
</style>
