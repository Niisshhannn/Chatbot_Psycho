<template>
  <div :class="cClass">
    <div class="avatar"></div>
    <div class="message" v-html="cMsg"></div>
  </div>
</template>

<script>
export default {
  props: {
    msg: {
      type: String,
      default: "",
    },
    dir: {
      type: String, // left or right
      default: "left",
    },
  },
  computed: {
    cClass() {
      // return the class name
      if (this.dir === "left") return "chat-left";
      return "chat-right";
    },
    cMsg() {
      return this.msg.replace("\n", "<br />");
    },
  },
  data() {
    return {};
  },
};
</script>

<style scoped>
.chat-left {
  width: 100%;
  display: flex;
}

.chat-right {
  width: 100%;
  display: flex;
  flex-direction: row-reverse;
}

.avatar {
  flex: 0 0 32px;
  width: 32px;
  height: 32px;
  background-color: red;
  border-radius: 50%;
  margin-right: 10px;
  background: url("~@/assets/avatar.jpg") no-repeat;
  background-size: cover;
  background-position: center center;
  box-sizing: border-box;
}

.message {
  max-width: 60%;
  min-height: 32px;
  background-color: #d9dee6;
  padding: 8px 15px;
  box-sizing: border-box;
  color: #081f4d;
  border-radius: 10px;
  border-top-left-radius: 0;
  word-wrap: break-word;
  word-break: break-all;
}

.message p {
  line-height: 1;
}

.chat-right .avatar {
  margin-right: 0;
  margin-left: 10px;
}

.chat-right .message {
  border-radius: 10px;
  border-top-right-radius: 0;
  background-color: #0a2866;
  color: #fff;
}
</style>
