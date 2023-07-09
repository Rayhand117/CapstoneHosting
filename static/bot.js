window.watsonAssistantChatOptions = {
  integrationID: "1fcf06f6-2d6f-46b3-85ba-58d4c32baee5", // The ID of this integration.
  region: "us-south", // The region your integration is hosted in.
  serviceInstanceID: "cce0e534-a5b6-4100-80fb-05ab07f9b4e3", // The ID of your service instance.
  onLoad: function(instance) { instance.render(); }
};
setTimeout(function(){
  const t=document.createElement('script');
  t.src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + (window.watsonAssistantChatOptions.clientVersion || 'latest') + "/WatsonAssistantChatEntry.js";
  document.head.appendChild(t);
});