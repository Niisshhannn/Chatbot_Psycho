<template>
  <div id="app">
    <intro-view class="intro-view" />
    <chat-view class="chat-view" />
  </div>
</template>

<script>
import ChatView from "./components/chat/index";
import IntroView from "./components/intro/index";

export default {
  name: "App",
  components: {
    ChatView,
    IntroView,
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  display: flex;
  justify-content: space-between;
}

.intro-view {
  flex: auto;
}

.chat-view {
  max-width: 32%;
  flex: auto;
}
</style>
