<template>
  <div class="container">
    <header>
      这是聊天页
    </header>

    <main ref="chatContent">
      <div class="content">
        <div v-for="(item, index) in msgList" :key="index" class="item">
          <chat-item :msg="item.msg" :dir="item.dir" />
        </div>
      </div>

      <chat-option
        v-show="showOptions && options.length > 0"
        class="options"
        :options="options"
        @choose="handleOption"
      />
    </main>

    <footer>
      <chat-input @send="handleSend" />
    </footer>
  </div>
</template>

<script>
import ChatItem from "./ChatItem";
import ChatInput from "./ChatInput";
import ChatOption from "./ChatOption";
import { apiChat } from "@/api";

export default {
  components: {
    ChatItem,
    ChatInput,
    ChatOption,
  },
  data() {
    return {
      msgList: [], // { msg: '', dir: 'left' }
      options: [],
      showOptions: true, // 是否展示选项
    };
  },
  watch: {
    msgList() {
      // 自动滚动末尾
      this.$nextTick(() => {
        const dom = this.$refs.chatContent;
        dom.scrollTo({
          top: dom.scrollHeight,
          behavior: "smooth",
        });
      });
    },
  },
  methods: {
    handleSend(value) {
      this.msgList.push({ msg: value, dir: "right" });

      apiChat(value).then((res) => {
        // 添加回复
        this.msgList.push({ msg: res.msg, dir: "left" });
      });
    },
    handleOption(value) {
      console.log(value);
    },
  },
};
</script>

<style scoped>
.container {
  position: relative;
  width: 100%;
  height: 100vh;
  box-sizing: border-box;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  border-left: 1px solid #ccc;
  border-right: 1px solid #ccc;
}

.container > header {
  flex: 0 0 45px;
  height: 45px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-bottom: 1px solid #ccc;
  box-shadow: 0 2px 6px 0 rgba(0, 0, 0, 0.1);
}

.container > main {
  flex: 1 1 auto;
  box-sizing: border-box;
  padding: 20px 12px 0;
  display: flex;
  flex-direction: column;
  overflow-x: hidden;
  overflow-y: auto;
}

.content {
  flex: 1 1 auto;
  box-sizing: border-box;
  padding-bottom: 12px;
}

.options {
  flex: 0 0 auto;
}

.container > footer {
  flex: 0 0 auto;
}

.item ~ .item {
  margin-top: 20px;
}
</style>
