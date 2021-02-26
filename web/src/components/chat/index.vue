<template>
  <div class="container">
    <header>{{ title }}</header>

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
      loading: false,
      msgList: [], // { msg: '', dir: 'left' }
      options: [],
      lang: "en", // 保存用户的语言
      type: "", // 用户选择的类型
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
  computed: {
    title() {
      if (!this.loading) return "Palette";
      if (this.lang === "zh") return "正在输入...";
      if (this.lang === "fr") return "écrit...";
      return "writing...";
    },
  },
  mounted() {
    // 第一句
    this.chat("#init");
  },
  methods: {
    chat(msg, lang, type) {
      // 调用接口
      this.loading = true;
      apiChat(msg, lang, type).then(this.handleResponse.bind(this));
    },
    handleSend(value) {
      this.msgList.push({ msg: value, dir: "right" });
      this.chat(value, this.lang, this.type);
    },
    handleOption(opt) {
      const { key } = opt;
      if (["fr", "zh", "en"].includes(key)) {
        // 说明用户在选语言
        this.lang = key;
        this.chat("#lang", key);
      } else {
        // 说明用户在选别的东西
        this.type = key;
        this.chat("#type", this.lang, key);
      }
    },
    // 处理chatbot的回复
    handleResponse(res) {
      this.loading = false;
      const { msg, options = [] } = res;
      this.msgList.push({ msg: msg, dir: "left" });
      this.options = options;
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
